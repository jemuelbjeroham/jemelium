import subprocess
import sys

# Define EM servers and config agent for SAT and DFW datacenters
sat_servers = ["testbat11lsat", "testbat13l", "testbat14l"]
dfw_servers = ["testbat11ldfw", "testbat13ldfw", "testbat14ldfw"]
sat_config_agent = "testbat12lsat"
dfw_config_agent = "testbat12ldfw"

# Define the paths for the shell scripts to run at the target datacenter
target_preparation_scripts = [
    "/pt/ctm/script/preparation_script_1",
    "/pt/ctm/script/preparation_script_2",
    "/pt/ctm/script/preparation_script_3",
]

# Dictionary mapping each script name to its specific path
script_paths = {
    "stopme": "/pt/ctm/script/stopme",
    "startme": "/pt/ctm/script/startme",
    "statme": "/pt/ctm/script/statme",
    "stop_config_agent": "/pt/ctm/script/stop_config_agent",
    "start_config_agent": "/pt/ctm/script/start_config_agent",
}


def execute_script(server, script_key):
    """Execute a shell script on a remote server with a specified path."""
    script_path = script_paths.get(script_key)
    if not script_path:
        print("Error: Script path for {} not found.".format(script_key))
        sys.exit(1)
        
    cmd = "ssh ecs@{} '{}'".format(server, script_path)
    try:
        print("Executing command: {}".format(cmd))
        output = subprocess.check_output(cmd, shell=True)
        print(output)
        return output
    except subprocess.CalledProcessError as e:
        print("Error executing command on {}: {}".format(server, e))
        sys.exit(1)


def execute_target_preparation_scripts(target):
    """Run the three preparation scripts on the target datacenter."""
    for script in target_preparation_scripts:
        cmd = "ssh ecs@{} '{}'".format(target, script)
        try:
            print("Executing preparation script: {}".format(script))
            output = subprocess.check_output(cmd, shell=True)
            print(output)
        except subprocess.CalledProcessError as e:
            print("Error executing preparation script {}: {}".format(script, e))
            sys.exit(1)


def user_confirmation(prompt):
    """Prompt the user for confirmation to proceed with an action."""
    while True:
        choice = input(f"{prompt}\n1: Yes 2: No\n")
        if choice == "1":
            return True
        elif choice == "2":
            print("Action cancelled by user. Previous steps are not rolled back.")
            print("Please manually check the state of the system before proceeding.")
            input("Press Enter to exit the script and check manually.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1 or 2.")


def stop_em_servers(servers):
    """Stop EM servers in the given order with user confirmation."""
    for server in servers:
        if user_confirmation(f"Can I issue stopme for server {server}?"):
            execute_script(server, "stopme")


def start_em_servers(servers):
    """Start EM servers in the given order with user confirmation."""
    for server in servers:
        if user_confirmation(f"Can I issue startme for server {server}?"):
            execute_script(server, "startme")


def check_em_servers_down(servers):
    """Check that all EM servers are down with user confirmation."""
    for server in servers:
        if user_confirmation(f"Can I issue statme for server {server} to confirm it is down?"):
            output = execute_script(server, "statme")
            if "down" not in output.lower():
                print("Error: Server {} is still running.".format(server))
                sys.exit(1)
            print("Server {} is confirmed down.".format(server))


def perform_dr(source, target, source_servers, target_servers):
    """Perform DR process from source datacenter to target datacenter with user confirmations."""
    # Step 1: Stop config agent in the source datacenter
    if user_confirmation(f"Can I issue stop_config_agent on {source}?"):
        execute_script(source, "stop_config_agent")

    # Step 2: Stop EM servers in the source datacenter
    stop_em_servers(source_servers)

    # Step 3: Check all EM servers are down in the source datacenter
    check_em_servers_down(source_servers)

    # Step 4: Confirm to proceed to the target datacenter
    if user_confirmation(f"All servers are down in {source}. Can we move to {target} for DR?"):
        # Step 5: Run preparation scripts in the target datacenter
        execute_target_preparation_scripts(target)

        # Step 6: Start EM servers in the target datacenter
        start_em_servers(target_servers)

        # Step 7: Start config agent in the target datacenter
        if user_confirmation(f"Can I issue start_config_agent on {target}?"):
            execute_script(target, "start_config_agent")


def select_dr_direction():
    """Prompt the user to select the DR direction."""
    print("Select the DR direction:")
    print("1: SAT to DFW")
    print("2: DFW to SAT")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            return "sat_to_dfw"
        elif choice == "2":
            return "dfw_to_sat"
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    print("Starting DR Automation Script")
    direction = select_dr_direction()

    if direction == "sat_to_dfw":
        print("Starting DR process: SAT to DFW")
        perform_dr(sat_config_agent, dfw_config_agent, sat_servers, dfw_servers)
    elif direction == "dfw_to_sat":
        print("Starting DR process: DFW to SAT")
        perform_dr(dfw_config_agent, sat_config_agent, dfw_servers, sat_servers)

    print("DR process completed successfully.")

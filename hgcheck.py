import subprocess
import os

# Configurations
HG_SCRIPT_PATH = "/ecs_share/scripts/utils/jobs/hg_aglist/clean_ocp_hg.sh"  # Path to hg_aglist script
HOSTGROUP_NAME = "TALONBATCH"  # Talon host group name
DELETE_COMMAND_TEMPLATE = "ctm config server:hostgroup:agent::delete {server} {hostgroup} {hostname}"


def get_hostgroup_agents():
    """Run the hg_aglist script to fetch the hostgroup agents."""
    try:
        output = subprocess.check_output([HG_SCRIPT_PATH], stderr=subprocess.STDOUT)
        hostgroup_agents = [line.strip() for line in output.splitlines() if line.strip()]
        return hostgroup_agents
    except subprocess.CalledProcessError as e:
        print("Error executing hg_aglist script:", e.output)
        return []


def validate_and_cleanup(hostgroup_agents):
    """Check for invalid hosts and remove them."""
    predefined_hosts = [
        "v2-ctm-agent-0-tocp4sat03",
        "v2-ctm-agent-2-tocp4sat03",
        "v2-ctm-agent-1-tocp4sat03",
        "v2-ctm-agent-0-tocp4dfw03",
        "v2-ctm-agent-1-tocp4dfw03",
        "v2-ctm-agent-2-tocp4sat03"
    ]
    
    invalid_hosts = []
    for agent in hostgroup_agents:
        if agent not in predefined_hosts:
            invalid_hosts.append(agent)
    
    if not invalid_hosts:
        print("No host is added. Host group {} is good.".format(HOSTGROUP_NAME))
        return
    
    for host in invalid_hosts:
        remove_host(host)


def remove_host(hostname):
    """Remove the invalid host using CLI API command."""
    server = "rsTEST2"  # Update with the correct server name if needed
    try:
        delete_command = DELETE_COMMAND_TEMPLATE.format(server=server, hostgroup=HOSTGROUP_NAME, hostname=hostname)
        os.system(delete_command)
        print("Removed invalid host: {} from host group {}".format(hostname, HOSTGROUP_NAME))
    except Exception as e:
        print("Failed to remove host {}: {}".format(hostname, e))


def main():
    """Main script execution."""
    print("Fetching host group agents...")
    hostgroup_agents = get_hostgroup_agents()
    if not hostgroup_agents:
        print("No agents found in the host group.")
        return
    
    print("Validating agents in the host group...")
    validate_and_cleanup(hostgroup_agents)


if __name__ == "__main__":
    main()



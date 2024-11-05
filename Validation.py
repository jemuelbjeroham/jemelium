import subprocess

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1: Pre Validation")
        print("2: Post Validation")
        print("3: Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            server_menu("pre")
        elif choice == '2':
            server_menu("post")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def server_menu(validation_type):
    while True:
        print("\nChoose a server:")
        print("1: testbat11lsat")
        print("2: testbat12lsat")
        print("3: testbat13l")
        print("4: testbat14l")
        print("5: Previous menu")
        server_choice = input("Enter your choice: ")

        if server_choice == '1':
            execute_script_on_server("testbat11lsat", validation_type)
        elif server_choice == '2':
            execute_script_on_server("testbat12lsat", validation_type)
        elif server_choice == '3':
            execute_script_on_server("testbat13l", validation_type)
        elif server_choice == '4':
            execute_script_on_server("testbat14l", validation_type)
        elif server_choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def execute_script_on_server(server, validation_type):
    # Paths to validation scripts
    pre_validation_script = "/shared/scripts/pre_validation_script.sh"
    post_validation_script = "/shared/scripts/post_validation_script.sh"

    # Choose the appropriate script
    script = pre_validation_script if validation_type == "pre" else post_validation_script

    print(f"\nConnected to {server}.")
    print("Do you want to run the script? (1: Yes, 2: No)")
    run_choice = input("Enter your choice: ")

    if run_choice == '1':
        try:
            print(f"Running script on {server}...")
            # Use SSH to run the script on the remote server
            result = subprocess.run(["ssh", f"ecs@{server}", "bash", "-c", f"'{script}'"],
                                    capture_output=True, text=True)

            # Output the result of the script execution
            if result.returncode == 0:
                print(f"Script executed successfully on {server}.")
                print(result.stdout)
            else:
                print(f"Script execution failed on {server}.")
                print(result.stderr)
        except Exception as e:
            print(f"An error occurred while running the script on {server}: {e}")
    elif run_choice == '2':
        print("Returning to previous menu.")
    else:
        print("Invalid choice. Returning to previous menu.")

# Run the main menu
if __name__ == "__main__":
    main_menu()

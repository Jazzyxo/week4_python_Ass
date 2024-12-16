def modify_file_content(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, "r") as infile:
            lines = infile.readlines()  # Read all lines from the input file
        
        # Open the output file for writing
        with open(output_file, "w") as outfile:
            for i, line in enumerate(lines, start=1):
                # Add line numbers to each line
                modified_line = f"{i}: {line}"
                outfile.write(modified_line)  # Write the modified line to the output file
        
        print(f"File has been successfully modified and saved to '{output_file}'!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main program
if __name__ == "__main__":
    # Ask the user for the input file name
    input_filename = input("Enter the name of the file to read: ")
    output_filename = "modified_" + input_filename  # Output file name
    
    # Call the function to modify the file content
    modify_file_content(input_filename, output_filename)

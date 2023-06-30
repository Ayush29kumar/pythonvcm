import subprocess

def festival_tts(text):
    command = f'(voice_cmu_us_rms_cg) (SayText "{text}")'
    festival_process = subprocess.Popen(['festival', '--pipe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    # Send the command to Festival
    festival_process.stdin.write(command.encode())
    festival_process.stdin.flush()

    # Wait for Festival to finish speaking and capture the output
    output, _ = festival_process.communicate()

    # Terminate the Festival process
    festival_process.terminate()

    # Decode the output from bytes to string
    output = output.decode()

    return output

# Example usage
text = " "
output = festival_tts(text)
print(output)

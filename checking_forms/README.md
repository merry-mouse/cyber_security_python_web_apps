# Requirements

## Create virtual env and install requests

This code requires requests library installed. First create virtual env using this command:

```bash
python -m venv .env
```

and then activate it and and install necessary libraries:

```bash
source /.env/bin/activate
pip install -r requirements.txt
```

Start the Server in a separate terminal: Run the following command to start a local web server. By default, this will serve files from the current directory on port 8000.

```bash
python -m http.server
```

# Running the script

If you are on a Unix/Linux system (including Mac OS) you can run this command

```bash
chmod a+x checker.py
```

to make this file executable, and then you can run it like this

```bash
./check.py http://127.0.0.1:8000
```

The chmod a+x checker.py command changes the permissions of the file checker.py to make it executable. This command is necessary because, by default, files may not have permission to be executed as programs in Unix-like operating systems, including Linux and macOS.

Here's a breakdown of what chmod a+x checker.py does:

- chmod: Stands for "change mode", and it's used to change the access permissions of file system objects (files and directories).
- a+x:
  - a stands for "all". This means the change applies to all users (the file owner, the group members, and others).
  - +x adds execute permission. x is for execute, + means add this permission.
- checker.py: The name of the file whose permissions you're changing.

So, `chmod a+x checker.py` makes `checker.py` executable by anyone who has access to the file. This allows you to run the script directly from the terminal using ./checker.py instead of needing to prefix it with the python interpreter explicitly every time.

# Requirements

## Create virtual env and install requests

This code requires requests library installed. First create virtual env using this command:

```bash
python -m venv .env
```

and then activate it and and install requests:

```bash
source /.env/bin/activate
pip install requests
```

after that you can run python file and check if the password was pawned with a command like this:

```bash
python checker.py some_password_to_check
```

## if you want to run file without virtual env activation in the future

If you want to be able to run the script without activating virtualev where requests library is located and don't want to install it locally, you can add shebang line at the top of the file. It should be a path to the enterpreter and must start with `#!`. It can look like this: `#!/usr/bin/env/python3.11`

# Running the script

If you are on a Unix/Linux system (including Mac OS) you can run this command

```bash
chmod a+x checker.py
```

to make this file executable, and then you can run it like this

```bash
./checker.py password_to_check
```

The chmod a+x checker.py command changes the permissions of the file checker.py to make it executable. This command is necessary because, by default, files may not have permission to be executed as programs in Unix-like operating systems, including Linux and macOS.

Here's a breakdown of what chmod a+x checker.py does:

- chmod: Stands for "change mode", and it's used to change the access permissions of file system objects (files and directories).
- a+x:
  - a stands for "all". This means the change applies to all users (the file owner, the group members, and others).
  - +x adds execute permission. x is for execute, + means add this permission.
- checker.py: The name of the file whose permissions you're changing.

So, `chmod a+x checker.py` makes `checker.py` executable by anyone who has access to the file. This allows you to run the script directly from the terminal using ./checker.py instead of needing to prefix it with the python interpreter explicitly every time.

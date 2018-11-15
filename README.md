# GoTo
Python script to create shortcut for terminal navigation

## Commands
- goto --add [name] [path]: adds new path shortcut, if name already exists, overrides
- goto --remove [name]: removes a shortcut
- source goto [name]: goes to added directory using the name. **Only here need to call first the source command because terminal runs in subprocess**
- goto --list: lists all shortcuts
- goto --help: lists all commands

### Installing
Run ```install.py``` to configure script to call directly, from anywhere

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
# AirBnB Clone - The Console

## Description
First step of the AirBnB clone: a command interpreter (`console.py`) that
manages AirBnB objects (`BaseModel`, `User`, `State`, `City`, `Amenity`,
`Place`, `Review`) and persists them in a JSON file (`file.json`) through a
`FileStorage` engine.

Serialization flow:
`Instance <-> dict <-> JSON string <-> file`

## Structure
- `console.py` - the command interpreter (`HBNBCommand`)
- `models/base_model.py` - `BaseModel`, parent of all classes
- `models/{user,state,city,amenity,place,review}.py` - model classes
- `models/engine/file_storage.py` - `FileStorage` (JSON persistence)
- `tests/` - unit tests (`unittest`)

## Starting the interpreter
Interactive:
```
$ ./console.py
(hbnb) help
```
Non-interactive:
```
$ echo "help" | ./console.py
```

## Commands
| Command | Usage |
|---|---|
| `help` | `help [command]` |
| `quit` / `EOF` | exit the program |
| `create` | `create <class name>` - creates, saves, prints the id |
| `show` | `show <class name> <id>` |
| `destroy` | `destroy <class name> <id>` |
| `all` | `all` or `all <class name>` |
| `update` | `update <class name> <id> <attribute name> "<attribute value>"` |

## Examples
```
(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907
(hbnb) update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-...) {'first_name': 'Betty', ...}
(hbnb) all User
(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```

## Tests
```
python3 -m unittest discover tests
```

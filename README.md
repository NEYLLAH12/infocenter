# InfoCenter

InfoCenter is a command-line utility written in Python that allows you to quickly change file attributes such as read-only, hidden, or system across multiple files on Windows systems.

## Features

- Change the read-only attribute of files.
- Change the hidden attribute of files.
- Change the system attribute of files.
- Process multiple files at once.

## Requirements

- Python 3.x
- Windows OS (as it uses Windows-specific file attributes)

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/InfoCenter.git
   ```

2. Navigate to the cloned directory:

   ```shell
   cd InfoCenter
   ```

## Usage

Run the script using Python, specifying the files and desired attributes:

```shell
python InfoCenter.py [options] <file1> <file2> ...
```

### Options

- `--read-only`: Set files to read-only.
- `--not-read-only`: Unset read-only attribute.
- `--hidden`: Set files to hidden.
- `--not-hidden`: Unset hidden attribute.
- `--system`: Set files to system.
- `--not-system`: Unset system attribute.

### Example

To set files `example1.txt` and `example2.txt` to read-only and hidden:

```shell
python InfoCenter.py --read-only --hidden example1.txt example2.txt
```

To remove the read-only attribute from `example1.txt`:

```shell
python InfoCenter.py --not-read-only example1.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Authors

- Your Name - [Your GitHub Profile](https://github.com/yourusername)
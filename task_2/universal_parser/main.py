import argparse
import configparser
from universal_parser.serializer_factory import SerializerFactory
from universal_parser.logger.logger import init_logger
import os

logger = init_logger(__name__)


def main():
    def parse(new_format: str, file_path: str):
        factory = SerializerFactory()

        old_format = os.path.splitext(str(file_path))[-1].replace(".", "")
        if old_format == new_format:
            raise ValueError(f"Old and new formats are same, both are .{new_format}")

        old_format_parser = factory.get_serializer(old_format)
        new_format_parser = factory.get_serializer(new_format)

        py_object = old_format_parser.load(file_path)

        os.remove(file_path)
        new_format_parser.dump(
            py_object, file_path.rsplit(".", 1)[0] + "." + new_format.lower()
        )
        logger.info(
            f"Success convertation: {file_path} -> {file_path.rsplit('.', 1)[0]+'.'+ new_format.lower()}"
        )

    try:
        parser = argparse.ArgumentParser(description="JSON/TOML/YAML/PICKLE Serializer")

        parser.add_argument(
            "-config",
            "--config_file",
            type=str,
            help="configuration file with instructions",
        )
        parser.add_argument(
            "-new",
            "--new_format",
            type=str,
            help="new format of your file",
        )
        parser.add_argument("-file", "--file_path", type=str, help="path to your file",)

        args = parser.parse_args()
        
        if not None in (args.file_path, args.config_file):
            if not os.path.exists(args.file_path):
                if not os.path.exists(args.config_file):
                    raise ValueError(f"Configuration file {args.config_file} doesn't exist")

        if args.config_file is not None:
            config = configparser.ConfigParser()
            config.read(args.config_file)
            new_format = config["Serializer"]["new_format"]
            file_path = config["Serializer"]["file_path"]
        else:
            new_format = args.new_format
            file_path = args.file_path

        if None in (new_format, file_path):
            raise ValueError("Some arguments left unfilled")
        elif not new_format:
            raise ValueError("New format isn't specified.")
        elif not os.path.exists(file_path):
            raise ValueError(f"{file_path} doesn't exist")

        parse(new_format, file_path)

    except Exception as error:
        logger.error(error, exc_info=True)

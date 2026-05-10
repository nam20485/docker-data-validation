import sys
import json


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate.py <path_to_file>")
        return 1

    with open(sys.argv[1], "r") as f:
        for line_num, line in enumerate(f, start=1):
            try:
                j = json.loads(line)
                prompt = j["prompt"]
                completion = j["completion"]
                token_length = j["token_length"]
                if not isinstance(prompt, str) or len(prompt) == 0:
                    print(f"Invalid prompt: {prompt} on line number:{line_num}")
                    return 1
                if not isinstance(completion, str):
                    print(f"Invalid completion: {completion} on line number:{line_num}")
                    return 1
                if not isinstance(token_length, int) or token_length <= 0:
                    print(
                        f"Invalid token_length: {token_length} on line number:{line_num}"
                    )
                    return 1
            except KeyError as e:
                print(f"Missing field: {e} on line number:{line_num}")
                return 1
            except json.JSONDecodeError as e:
                print(f"Invalid JSON: {e} on line number:{line_num}")
                return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

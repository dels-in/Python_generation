import requests
import os
import zipfile


def create_task_structure(module_folder, task_number):
    task_folder_name = f"task{task_number}"
    task_folder_path = os.path.join(module_folder, task_folder_name)

    if not os.path.exists(task_folder_path):
        os.makedirs(os.path.join(task_folder_path, "tests"), exist_ok=True)

    task_file_path = os.path.join(task_folder_path, f"task{task_number}.py")
    if not os.path.exists(task_file_path):
        with open(task_file_path, 'w'):
            pass
    return os.path.join(task_folder_path, "tests")


def download_and_extract_zip(url, extract_to):
    try:
        zip_path = os.path.join(extract_to, "downloaded.zip")
        response = requests.get(url)

        if response.status_code == 200:
            with open(zip_path, 'wb') as file:
                file.write(response.content)
        else:
            print(
                f"Ошибка при скачивании файла: статус-код {response.status_code}")
            return

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        os.remove(zip_path)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании файла: {e}")

    except zipfile.BadZipFile as e:
        print(f"Ошибка при распаковке файла: {e}")


def create_description(description, module_folder, task_number):
    task_folder_name = f"task{task_number}"
    task_folder_path = os.path.join(module_folder, task_folder_name)
    task_file_path = os.path.join(task_folder_path, f"task{task_number}.md")
    if not os.path.exists(task_file_path):
        with open(task_file_path, 'w') as f:
            print(description, file=f)


if __name__ == "__main__":
    folder, number = input("Enter task's folder path to a learning module and a number of solution's file: ").split()
    folder = f"part{folder}"
    task_url = input("Enter url: ")

    print("Enter description: ")
    description = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        description.append(line)
    description = "\n".join(description)

    tests_folder_name = create_task_structure(folder, number)
    download_and_extract_zip(task_url, tests_folder_name)
    create_description(description, folder, number)

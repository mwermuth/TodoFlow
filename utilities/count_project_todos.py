from config import projects_path

done_tag = ' @done'

def count_inbox():
    with open(projects_path, "r") as f:
        count = 0
        for line in f:
            line = line.strip()
            if line.startswith('_'):
                break
            if line.startswith('-') and (line.find(done_tag) == -1):
                count += 1
        if count:
            print(count)
        else:
            print(" ")

count_inbox()

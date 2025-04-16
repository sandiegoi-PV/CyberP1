# "HASH_CRACKER USED DICTIONARY ATTACK!"
# if it succeeds the menu will say "it's a critical hit!" if not the menu will say "it wasn't very effective"
import hashlib
from encodings.utf_8_sig import encode


def hash_tester(hash,dictionary):
    did_it_work = 0
    # if taking into account other hashes we would first test to see what version hash it is
    # then compare it to hashed words in the dictionary
    for word in dictionary:
        if hashlib.sha256((word).encode()).hexdigest() == hash:
            print(f"hash matched: {word}")
            did_it_work = 1
            break

    if did_it_work == 0:
        print("it didn't work")
    else:
        print("yay it worked")

    return


def main():
    with open("/Users/sandiegoi/PycharmProjects/CyberP1/Wordlist/rockyou.txt", "r", encoding= "utf-8", errors="ignore") as file:
        #a 'with' statement will close the file when I'm done, even if there are errors

        words = [line.strip() for line in file]
        #this is called list comprehension. Not previously familiar. The single line is a compressed version of the four below
        #words = []                    # Step 1: Start with an empty list
        #for line in file:            # Step 2: Loop through the file line by line
        #clean_line = line.strip()  # Step 3: Remove newline characters
        #words.append(clean_line)   # Step 4: Add the clean line to the list
    ex_hash = hashlib.sha256(("billy").encode()).hexdigest()
    hash_tester(ex_hash,words)
    return

if __name__ == "__main__":
    main()
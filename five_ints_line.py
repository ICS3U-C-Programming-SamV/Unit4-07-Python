#!/usr/bin/env python3
# Created By: Sam V
# Date: Nov 25th, 2026
#!/usr/bin/env python3
# Created by: Your Name
# Created on: November 2026
# This program prints the integers from 1000 to 2000, five per line.


def main():
    # Loop through all integers from 1000 to 2000
    for counter in range(1000, 2001):
        # Print a newline after every 5th integer
        if (counter + 1) % 5 == 0:
            print(counter)
        else:
            print(counter, end=" ")

    print("\nThat's all!")


if __name__ == "__main__":
    main()

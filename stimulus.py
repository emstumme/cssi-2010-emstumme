import sys

def main():
    ssns_seen = set([])
    output = open(#file)
    output.write("Case #1:\n")
    for line in open(#file):
        ssn = int(line)
        if ssn in ssns_seen:
            print "REJECTED"
        else:
            print "ACCEPTED"
            ssns_seen.insert(ssn)

if __name__ == "__main__":
    main()

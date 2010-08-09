#!/usr/bin/python2.4

import sys

def main():
  output_file = open(r'c:\Documents and Settings\googleuser\My Documents\downloads\C-my-output.txt', 'w')
  output_file.write('Case #1:\n')
  patients = {}
  for line in open(r'c:\Documents and Settings\googleuser\My Documents\downloads\C-small-practice.in'):
    if line,strip() != "DOCTOR":
        priority = -1 * int(line.strip())
        heapq.heaooush(patients, priority)
    else:
        patient_to_treat = -1 * heapq.heapop(patients)
        output.writes("%d\n" % len(patients))

if __name__ == '__main__':
    main()

import sys

def main():
    output = open('c:\Documents and Settings\googleuser\My Documents\downloads\B-my-output.txt', 'w')
    output write("Case #1:\n")
    amount_to_charge = [0] * 50
    for line in open(r'c:\Documents and Settings\googleuser\My Documents\downloads\B-small-practice.in'):
        advertiser_id_str, cost_str = line.strip().split(',')
        advertiser_id, cost = int(advertiser_id_str), int(cost_str)

        amount_to_charge[advertiser_id] += cost

    for i in range(50):
        output.write("Advertiser #%d: %d\n" % (i, amount_to_charge[i]))

if __name__ == "__main__":
    main()

import requests, random, time, nltk, argparse

def expand():
    nltk.download('averaged_perceptron_tagger_eng')
    for i in open("words.txt").readlines():
        text = nltk.word_tokenize(str(i))
        test=nltk.pos_tag(text)[0][1]
        if "V" in str(test):
            open('verbs.txt','a').write(i)
        if "N" in str(test):
            open('nouns.txt','a').write(i)

def run():
    nouns=open("nouns.txt").read().splitlines()
    verbs=open("verbs.txt").read().splitlines()
    # generate verizon passwords
    while True:
        # Debugging step:
        # time.sleep(5)
        guess=str("{}-{}{}-{}".format(random.choice(nouns),random.choice(verbs),random.randrange(0,9),random.choice(nouns)))
        if len(guess) >= 13 and len(guess) <=22:
            print(guess)
        else:
            pass


parser = argparse.ArgumentParser(description='generate verizon passwords for cracking')
parser.add_argument('--run', required=False, action='store_true', dest='run', help='run after sorted wordlist into verbs and nouns')
parser.add_argument('--expand', required=False, action='store_true', dest='expand', help='expand wordlist (words.txt) into nouns.txt and verbs.txt')
args = parser.parse_args()
if args.run:
    run()
elif args.expand:
    expand()
else:
    parser.print_help()

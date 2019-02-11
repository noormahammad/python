#!/user/bin/python

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        options, args = getopt.getopt(argv,"h:i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('commandline-args-options.py -i <inputfile> -o <outputfile')
        sys.exit(2)
    
    for option, arg in options:       
        if(option == "-h"):
            print("commandline-args-options.py -i <inputfile> -o <outputfile>")
        elif option in ("-i", "--ifile"):
            inputfile = arg
        elif option in ("-o", "--ofile"):
            outputfile = arg
    
    print("Input file is", inputfile)
    print("Output file is ", outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
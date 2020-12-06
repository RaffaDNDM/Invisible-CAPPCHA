import NeuralNetwork as nn
import colorama
import argparse
from termcolor import cprint
import utility

def args_parser():
    '''
    Parser of command line arguments
    
    Returns:
        plot (bool): If True, it plots data already acquired 
                     instead of acquire new audio files
        
        record (bool): If True, it record audio during key logging
        
        extract (bool): If True, it extract features from data already
                        acquired instead of acquire new audio files
        
        file (str): Path of the file that you want to plot or from
                    which you want to extract features
        
        dir (str): Path of the folder where:
                   [-r option]
                     there will be stored audio files acquired
                     from the recorder and the keylogger
                   [-p option and -e option]
                     there are already recored audio on which
                     extraction and plot will be applied

        output (str): Path of the output folder in which graphics
                      will be stored as image
    '''
    #Parser of command line arguments
    parser = argparse.ArgumentParser()
    
    #Initialization of needed arguments
    parser.add_argument("-test", 
                        dest="test", 
                        help="""If specified, it performs test on specified
                                dataset using csv model of trained NN""",
                        action='store_true')
    
    parser.add_argument("-dir","-d",
                        dest="dir", 
                        help="""Path of the folder that contains the csv files of 
                                dataset and labels dictionary and contains/will
                                contain the json file of model""")

    #Parse command line arguments
    args = parser.parse_args()

    return args.test, args.dir


def select_option_feature():
    check = True
    while check:
        try:
            cprint(f'Select which type of features you want to use:\n{utility.LINE}', 'blue')
                
            for i in range(0, len(utility.OPTIONS)):
                cprint(f'{i})', 'yellow', end=' ')
                print(f'{utility.OPTIONS[i]}')

            cprint(f'3)', 'yellow', end=' ')
            print(f'All the features')
            cprint(f'{utility.LINE}', 'blue')

            option = int(input())
            if option >= 0 and option <= len(utility.OPTIONS):
                check = False

        except ValueError:
            cprint('[VALUE ERROR]', 'color', end=' ')
            print('Insert a value of them specified in menu')

    return option


def main():
    #Initialize colored prints
    colorama.init()
    #Parser of command line arguments
    test_mode, folder = args_parser()

    option = select_option_feature()
    net = nn.NeuralNetwork(folder,option)
    cprint(utility.LINE, 'blue')
    print('Number of labels:', end=' ')
    cprint(len(net.labels), 'green')
    cprint(utility.LINE, 'blue')
    input('Type ENTER to see them in details')
    cprint(utility.LINE, 'blue')

    for key in net.labels.keys():
        cprint(f'{key}:', 'red', end=' ')
        cprint(f'{net.labels[key]}', 'yellow')

    cprint(utility.LINE, 'blue')
    input('Type ENTER to train/test the model')
    cprint(utility.LINE, 'blue')

    if test_mode:
        net.test()
    else:
        net.train()


if __name__=='__main__':
    main()
#its working
from data_processing import data_process_uci, data_process_oppo,  data_process_unimib 
from models.cnn import CNN_choose
from models.cnn_mix import MixCNN_choose
from models.adnn import adnn_choose
#changed

# model
def get_model(args):
    if args.model == 'cnn':
        model = CNN_choose(dataset = args.dataset, res=False)
        return model
    else:
        print('not exist this model')
    


def get_dataset(args):
    if args.dataset == 'uci':
        source_loader, target_loader = data_process_uci.prep_domains_ucihar(args, SLIDING_WINDOW_LEN=args.len_sw, SLIDING_WINDOW_STEP=int(0.5*args.len_sw))
    elif args.dataset == 'oppo':
        source_loader, target_loader = data_process_oppo.prep_domains_oppor(args, SLIDING_WINDOW_LEN=args.len_sw, SLIDING_WINDOW_STEP=int(0.5*args.len_sw))
    elif args.dataset == 'unimib':
        source_loader, target_loader = data_process_unimib.prep_domains_shar(args, SLIDING_WINDOW_LEN=args.len_sw, SLIDING_WINDOW_STEP=int(0.5*args.len_sw))
    else:
        print('not exist this dataset')


    return source_loader, target_loader
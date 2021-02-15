from torch.utils.data import ConcatDataset
#from .voc import VOCDataset
from .coco import COCODataset
from ssd.config.path_catlog import DatasetCatalog

_DATASETS = {
    #'VOCDataset' : VOCDataset,
    'COCODataset': COCODataset,
}


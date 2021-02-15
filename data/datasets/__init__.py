from torch.utils.data import ConcatDataset
from .voc import VOCDataset
from .coco import COCODataset

_DATASETS = {
    'VOCDataset' : VOCDataset,
    'COCODataset': COCODataset,
}
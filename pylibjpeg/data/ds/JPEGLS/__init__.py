"""1.2.840.10008.1.2.4.81 - JPEG-LS Lossy (Near-Lossless) Image Compression"""

INDEX = {
    'CT1_JLSN' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.80'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 512),
        'Columns' : ('US', 512),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 16),
        'HighBit' : ('US', 15),
        'PixelRepresentation' : ('US', 1),
        'RescaleIntercept' : ('DS', '-1024'),
        'RescaleSlope' : ('DS', '1'),
        'RetrieveURI' : ('UR', 'ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04'),
    },
    'MG1_JLSN' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.80'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 4664),
        'Columns' : ('US', 3064),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 12),
        'HighBit' : ('US', 11),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '2047'),
        'WindowWidth' : ('DS', '4095'),
        'RetrieveURI' : ('UR', 'ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04'),
    },
    'RG1_JLSN' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.80'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME1'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 1955),
        'Columns' : ('US', 1841),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 15),
        'HighBit' : ('US', 14),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '15000'),
        'WindowWidth' : ('DS', '30000'),
        'RetrieveURI' : ('UR', 'ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04'),
    },
    'RG2_JLSN' : {
        'TransferSyntaxUID' : ('UI', '1.2.840.10008.1.2.4.80'),
        'SamplesPerPixel' : ('US', 1),
        'PhotometricInterpretation' : ('CS', 'MONOCHROME2'),
        'PlanarConfiguration' : ('US', 0),
        'NumberOfFrames' : ('IS', '1'),
        'Rows' : ('US', 2140),
        'Columns' : ('US', 1760),
        'BitsAllocated' : ('US', 16),
        'BitsStored' : ('US', 10),
        'HighBit' : ('US', 9),
        'PixelRepresentation' : ('US', 0),
        'WindowCenter' : ('DS', '511'),
        'WindowWidth' : ('DS', '1024'),
        'RetrieveURI' : ('UR', 'ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04'),
    },
}

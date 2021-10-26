from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

#reading the sequence
record = SeqIO.read(r"C:\ReadMyCourse\PFB_practice\drug developement pipelines\covid_seq.gb", "genbank")

gd_diagram = GenomeDiagram.Diagram(record.id)
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

# for feature in record.features:
#     if feature.type != "CDS":
#         # Exclude this feature
#         continue
#     if len(gd_feature_set) % 2 == 0:
#         color = colors.blue
#     else:
#         color = colors.lightblue
#     gd_feature_set.add_feature(
#         feature, sigil="ARROW", color=color, label=True, label_size=14, label_angle=0
#     )

# I want to include some strandless features, so for an example
# will use EcoRI recognition sites etc.

#restriction site identification
restriction_map_data=[
    ("GAATTC", "EcoRI", colors.green),
    ("CCCGGG", "SmaI", colors.orange),
    ("AAGCTT", "HindIII", colors.red),
    ("GGATCC", "BamHI", colors.purple),
]
for site, name, color in restriction_map_data:
    index = 0
    while True:
        index = record.seq.find(site, start=index)
        if index == -1:
            break
        feature = SeqFeature(FeatureLocation(index, index + len(site)))
        gd_feature_set.add_feature(
            feature,
            color=color,
            name=str(index)+name,
            label=True,
            label_size=10,
            label_color=color,
            label_position=index
        )
        index += len(site)

import os
os.chdir(r"C:\ReadMyCourse\PFB Weekend Batch\day10")

gd_diagram.draw(format="linear", pagesize="A4", fragments=4, start=0, end=len(record))
gd_diagram.write("COVID_seq_restriction_gd_linear.pdf", "PDF")

gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize=(20 * cm, 20 * cm),
    start=0,
    end=len(record),
    circle_core=0.5,
)
gd_diagram.write("COVID_seq_restriction_gd_circular.pdf", "PDF")
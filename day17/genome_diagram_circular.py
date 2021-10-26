from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

#reading the sequence
record = SeqIO.read(r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day17\covid_seq.gb", "genbank")

gd_diagram = GenomeDiagram.Diagram(record.id)
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

for feature in record.features:
    if feature.type=="mat_peptide":
        if len(gd_feature_set) % 2 == 0:
            color = colors.red
        else:
            color = colors.yellow
        gd_feature_set.add_feature(
            feature, sigil="ARROW", color=color, label=True, label_size=20, label_angle=45
        )


import os
os.chdir(r"C:\learning\github\main\Python-for-Bioinfromatics-Oct-2021\day17")

gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize=(20 * cm, 20 * cm),
    start=0,
    end=len(record),
    circle_core=0.5,
)
gd_diagram.write("COVID_seq_restriction_gd_circular.pdf", "PDF")
setwd("~/work/phylostratr/ens_phylostr/biomart_data/plots")
library(ggplot2)
library(readr)
library(scales)
ToothGrowth$dose <- as.factor(ToothGrowth$dose)
head(ToothGrowth)

# Basic violin plot
p <- ggplot(ToothGrowth, aes(x=dose, y=len)) + 
  geom_violin()
p
# Rotate the violin plot
p + coord_flip()
# Set trim argument to FALSE
ggplot(ToothGrowth, aes(x=dose, y=len)) + 
  geom_violin(trim=FALSE)
# Change color by groups
dp <- ggplot(ToothGrowth, aes(x=dose, y=len, fill=dose)) + 
  geom_violin(trim=FALSE)+
  geom_boxplot(width=0.1, fill="white")+
  labs(title="Plot of length  by dose",x="Dose (mg)", y = "Length")
dp + theme_classic()



#read data
prot_combined_feats <- read_delim("~/work/phylostratr/ens_phylostr/biomart_data/ORF_feats.txt","\t", escape_double = FALSE, trim_ws = TRUE)
st<- factor(prot_combined_feats$Strata, levels = unique(prot_combined_feats$Strata))
#count occurence
table(unlist(prot_combined_feats$Strata))
new_labels<-c("cellular organisms:28059","Eukaryota:30061","Metazoa:23696", "Euteleostomi:14617",       "Mammalia:618","Theria:3976","Pimates:1287",          
              "Catarrhini:453","Hominidae:833", "Homininae:136","Homo sapiens:708","literature:884", "non-expressedORF:4022",   "expressedORF:1995")
#convert to log
prot_combined_feats$ProtLength<-log(prot_combined_feats$ProtLength)
#plot protlen
dp <- ggplot(prot_combined_feats, aes(x=st, y=ProtLength, fill=st)) + 
  geom_violin(trim=T)+ 
  geom_boxplot(width=0.1, fill="white",outlier.shape = NA)+
  labs(title="Prot length",x="Strata", y = "length(AA)")
dp + theme_classic()+ theme(text = element_text(size=20),
                            axis.text.x = element_text(angle=90, hjust=1))+scale_x_discrete(labels= new_labels)


#plot cdsGC
dp <- ggplot(prot_combined_feats, aes(x=st, y=GC_cds, fill=st)) + 
  geom_violin(trim=T)+ 
  geom_boxplot(width=0.1, fill="white",outlier.shape = NA)+
  labs(title="CDS GC%",x="Strata", y = "GC%")
dp + theme_classic()+ theme(text = element_text(size=20),
        axis.text.x = element_text(angle=90, hjust=1))+scale_x_discrete(labels= new_labels)



#make plots for ony ensembl data
ensembl_feats <- read_delim("~/work/phylostratr/ens_phylostr/biomart_data/ensembl_feat.txt","\t", escape_double = FALSE, trim_ws = TRUE)
st2<- factor(ensembl_feats$Strata, levels = unique(ensembl_feats$Strata))


#count occurence
table(unlist(ensembl_feats$Strata))
new_labels2<-c("cellular organisms:28059","Eukaryota:30061","Metazoa:23696", "Euteleostomi:14617", "Mammalia:618","Theria:3976","Pimates:1287",          
              "Catarrhini:453","Hominidae:833", "Homininae:136","Homo sapiens:708")

#plot gc content
dp <- ggplot(ensembl_feats, aes(x=st2, y=GeneGC, fill=st2)) + 
  geom_violin(trim=FALSE)+
  geom_boxplot(width=0.1, fill="white",outlier.shape = NA)+
  labs(title="Plot of GC content",x="Strata", y = "GC%")
dp + theme_classic()+ theme(text = element_text(size=20),
                            axis.text.x = element_text(angle=90, hjust=1))+scale_x_discrete(labels= new_labels2)
ensembl_feats$Tcount<-log(ensembl_feats$Tcount)
#plot tcount
dp <- ggplot(ensembl_feats, aes(x=st2, y=Tcount, fill=st2)) + 
  geom_violin(trim=FALSE)+
  geom_boxplot(width=0.1, fill="white",outlier.shape = NA)+
  labs(title="Plot of #transcripts",x="Strata", y = "#transcripts")
dp + theme_classic()+ theme(text = element_text(size=20),
                            axis.text.x = element_text(angle=90, hjust=1))+scale_x_discrete(labels= new_labels2)
ensembl_feats$Excount<-log(ensembl_feats$Excount)
#plot excount
dp <- ggplot(ensembl_feats, aes(x=st2, y=Excount, fill=st2)) + 
  geom_violin(trim=T)+
  geom_boxplot(width=0.1, fill="white",outlier.shape = NA)+
  labs(title="Plot of #exons",x="Strata", y = "#exons")
dp + theme_classic()+ theme(text = element_text(size=20),
                            axis.text.x = element_text(angle=90, hjust=1))+scale_x_discrete(labels= new_labels2)

#plot length
ensembl_feats$ProtLength<-log(ensembl_feats$ProtLength)
dp <- ggplot(ensembl_feats, aes(x=st2, y=ProtLength, fill=st2)) + 
  geom_violin(trim=T)+
  geom_boxplot(width=0.1, fill="white",outlier.shape = NA)+
  labs(title="Plot of length",x="Strata", y = "length(AA)")
dp + theme_classic()+ theme(text = element_text(size=20),
                            axis.text.x = element_text(angle=90, hjust=1))+scale_x_discrete(labels= new_labels2)

#mean of human cds
mean(ensembl_feats[ensembl_feats$Strata=='Homo sapiens',]$GC_cds)

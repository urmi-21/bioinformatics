setwd("~/work/phylostratr/ens_phylostr/biomart_data/plots")
library(ggplot2)
library(readr)
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


s_gc <- read_delim("~/work/phylostratr/ens_phylostr/biomart_data/plots/s_gc.txt", 
                   "\t", escape_double = FALSE, trim_ws = TRUE)

dp <- ggplot(s_gc, aes(x=St, y=gc, fill=St)) + 
  geom_violin(trim=FALSE)+
  geom_boxplot(width=0.1, fill="white")+
  labs(title="Plot of length  by dose",x="Dose (mg)", y = "Length")
dp + theme_classic()

#read data
prot_combined_feats <- read_delim("~/work/phylostratr/ens_phylostr/biomart_data/prot_combined_feats.txt","\t", escape_double = FALSE, trim_ws = TRUE)
prot_combined_feats$Strata <- factor(prot_combined_feats$Strata, levels = prot_combined_feats$Strata)
st<- factor(prot_combined_feats$Strata, levels = unique(prot_combined_feats$Strata)[1:5])

#plot gc content
dp <- ggplot(prot_combined_feats, aes(x=st, y=GeneGC, fill=st)) + 
  geom_violin(trim=FALSE)+
  geom_boxplot(width=0.1, fill="white")+
  labs(title="Plot of GC content",x="Strata", y = "GCcontent")
dp + theme_classic()

#plot tcount
dp <- ggplot(prot_combined_feats, aes(x=st, y=Tcount, fill=st)) + 
  geom_violin(trim=FALSE)+
  geom_boxplot(width=0.1, fill="white")+
  labs(title="Plot of #transcripts",x="Strata", y = "#transcripts")
dp + theme_classic()

#plot excount
dp <- ggplot(prot_combined_feats, aes(x=st, y=Excount, fill=st)) + 
  geom_violin(trim=FALSE)+
  geom_boxplot(width=0.1, fill="white")+
  labs(title="Plot of #exons",x="Strata", y = "#exons")
dp + theme_classic()


#plot protlen
dp <- ggplot(prot_combined_feats, aes(x=st, y=ProtLength, fill=st)) + 
  geom_violin(trim=T)+ coord_flip()+stat_ydensity(trim=T)+
  geom_boxplot(width=0.1, fill="white")+
  labs(title="Prot length",x="Strata", y = "length")
dp + theme_classic()

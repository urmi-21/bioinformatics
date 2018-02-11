/**********************************************
DATE:9-4-2014
Author: Urminder Singh
Description: Program which implements 
k-means clustering on n-dimentional data points. 


************************************************/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <time.h>
int K;
int size=0;
int choice=0;
float getdist(int, int,int);
float mod(float);


float **data;
int *carray,*cluster;
int main(int argc,char **argv){
int i,j,k,result=0,iterations=0;
int numlines=0,dimentions=0;
FILE *fp;
char line[100];

if(argc!=3){
printf("\nError in Arguments\nUsage is : arg1: input file, arg2: value of k");
return -1;
}
printf("\nEnter the choice for the distance function\n");
printf("\n0. Manhattan Distance");
printf("\n1. Euclidean Distance\n");
scanf("%d",&choice);
if(choice!=0 && choice !=1){
printf("Bad input choice,... Taking default as 1.\n");
choice=1;

}
K=atoi(argv[2]);
/********************************************
Read input data file
********************************************/
fp=fopen(argv[1],"r");
if(fp==NULL){
printf("\nPlease provide correct file name");
}

else{
//calculate num lines i.e. num of data points
 while(fgets(line, 80, fp) != NULL){
//	printf("%s",line);
	numlines++;	   
 }//end while
//calculate dimentions
for(i=0;i<strlen(line);i++){
	if(line[i]=='\n'){
		break;
	}	
	if(line[i]=='\t'){
		dimentions++;
	}
}//end for
dimentions++;
//put size=numlines
size=numlines;
printf("\ntotal lines=%d",numlines);
printf("\ntotal dimention=%d",dimentions);
/********************************************
Allocate memory to data
********************************************/
data = (float**) malloc(numlines*sizeof(float*));  
for ( i = 0; i < numlines; i++)  
   data[i] = (float*) malloc(dimentions*sizeof(float)); 


}//end else
/******************************************
enter data from input file to data matrix
******************************************/
rewind(fp);
int index=0,p=0;
char temp[10];
i=0;
j=0;
while(fgets(line, 100, fp) != NULL){
	printf("\n%s",line);

	
	for(k=0;k<strlen(line);k++){
		if(line[k]=='\n'){
			//break;
		}
		if(line[k]!=' ' && line[k]!='\t' && line[k]!='\n'){
			temp[index++]=line[k];
		}
		else if(line[k]=='\t' || line[k]==' ' || line[k]=='\n'){
			data[i][j++]=atof(temp);	
			//printf("\n**%f",data[i][j-1]);
			//clear temp array
			for(p=0;p<10;p++){
				temp[p]=' ';
			}//end for p
		}//end elif

	}//end for k
	
	i++;
	j=0;
	index=0;
}

fclose(fp);

//print data matrix
for(i=0;i<numlines;i++){
	printf("\n");
	for(j=0;j<dimentions;j++){
		printf("%.2f\t",data[i][j]);
	}

}
printf("\n dist1: %f",getdist(0,1,dimentions));

/*******************************************************
//choose starting centroids
********************************************************/
//init centroid array
/* Intializes random number generator */
 time_t t;
 srand((unsigned) time(&t));
carray=(int*)malloc(sizeof(int)*K);
//choose random K centroids
for(i=0;i<K;i++){
	int temp;
	if(i==0){	
		carray[i]=0 + rand() / (RAND_MAX / ((size-1) - 0 + 1) + 1);
	}
	else{
		temp=0 + rand() / (RAND_MAX / ((size-1) - 0 + 1) + 1);
		if(temp==carray[i-1]){
			temp=0 + rand() / (RAND_MAX / ((size-1) - 0 + 1) + 1);		
		}
		carray[i]=temp;		
	}
	//carray[i]=i;
}
printf("\n Choosing initial centroids...\n");
for(i=0;i<K;i++){
	printf("%d  ",carray[i]);
}

/***********************************************************
Start k means algorithm !!!
************************************************************/
cluster=(int*)malloc(sizeof(int)*size);

while(result!=1){
printf("=");
iterations++;
float minsum;
float dist[K],mindist;
float tempc[K];
int p,q,minindex;
//step 1 calculate distance of all points from clusters

for(i=0;i<size;i++){
	p=0;
	for(j=0;j<K;j++){
		dist[j]=getdist(i,carray[j],dimentions);
	//	printf("\ndist=%f",dist[j]);
	}//end for j

	//print distance
//	printf("\nDataPoint\tDistC1\tDistC2\tDistC3",i);
//	printf("\n%d\t",i);
	mindist=999999999;
	minindex=0;
	for(p=0;p<K;p++){
//		printf("%f \t",dist[p]);
		if(dist[p]<mindist){
			mindist=dist[p];
			minindex=p;		
		}
	}// end for p
	cluster[i]=carray[minindex];
	
	
	
}// end for i

/*print clusters*/

printf("\n");

for(i=0;i<K;i++){

	printf("\ncluster %d",i);
	for(j=0;j<size;j++){
		if(cluster[j]==carray[i]){
			printf("\n %d ---> %d",j,carray[i]);
		}
	}

}

/***********************************
re-compute centroids
***********************************/
float sumdist[size];
for(i=0;i<K;i++){
	for(j=0;j<size;j++){
		
		if(cluster[j]==carray[i]){
			sumdist[j]=0;
			//printf("\n** %d ---> %d",j,carray[i]);
			for(p=0;p<size;p++){
				if(cluster[p]==carray[i]){
					//printf("\n*** %d ---> %d",p,carray[i]);
					sumdist[j]=sumdist[j]+getdist(j,p,dimentions);
				}			
			}//end for p
		}// end outer if
	}// end for j


}//end for i


for(i=0;i<K;i++){
	minindex=999999999;
	minsum=999999999;
	minindex=carray[i];
	for(j=0;j<size;j++){
		if(cluster[j]==carray[i]){
			if(sumdist[j]<minsum){
				minindex=j;
				//printf("\nminindex is:%d",minindex);
				minsum=sumdist[j];
			}// end if
		}// end if
		if(cluster[j]!=carray[i]){
			//printf("\n1. Error");
			//printf("\n%d  %d",cluster[j],carray[i]);
			
		}
	}// end for j
	//update cluster index
	//printf("\nminindex is:%d",minindex);
	tempc[i]=minindex;
	
	
} // end for i

//print new centroids

int cflag=1;
for(i=0;i<K;i++){
	if(tempc[i]==carray[i]){
		cflag=1;
	}
	else{
		cflag=0;
		break;
	}
	
}

//no change in centroids
if(cflag==1){
result=1;

//print data with cluster points
/*
printf("\nFinal Clustering results\n\nDataPoint\t\tCluster Centroid");
for(i=0;i< size;i++){
	printf("\n%d\t\t%d",i,cluster[i]);

}// end for
*/
printf("\nK means Done in %d iterations!!\n Terminating now",iterations);
printf("\n Final centroids are data points:\n");
for(i=0;i<K;i++){
	printf("%d\t",carray[i]);
}

/*printf("\nclusters=");
for(i=0;i<size;i++){
	printf("\n%d\t",cluster[i]);
}
*/

}// end if

else{   printf("\nNew Centroids are:");
	for(i=0;i<K;i++){
		carray[i]=tempc[i];
		printf("%d  ",carray[i]);
	}
}

}//end while

//write the result file

fp=fopen("clusters.txt","w");
int cluster_num;
for(i=0;i<size;i++){
	//calculate cluster number to write to file
	for(j=0;j<K;j++){
		if(cluster[i]==carray[j]){
			cluster_num=j+1;
			break;
		}
	}
	fprintf(fp,"%d\n",cluster_num);

}
fclose(fp);
printf("\nfile clusters.txt written!!");

//print cluster points to separate files

char fname[5]={'c','l','-','a','\0'};
for(i=0;i<K;i++){
	
	

//	printf("\n%c",(char)(i));
	
	fp=fopen(fname,"w");

	for(j=0;j<size;j++){
		if(cluster[j]==carray[i]){
			for(k=0;k<dimentions;k++){
				fprintf(fp,"%f\t",data[j][k]);	
			}
			fprintf(fp,"\n");			
		}
	}

	fclose(fp);

	fname[3]++;
}




//calculate inter-cluster distances
float intercdist[K][K];
printf("\n");
printf("\nCalculating Inter and Intra cluster Distances...\n");
printf("\nDistance between centroids:\n");
for(i=0;i<K;i++){
	for(j=0;j<K;j++){
		intercdist[i][j]=getdist(carray[i],carray[j],dimentions);
		printf("%f\t",intercdist[i][j]);
	}printf("\n");

}
printf("\n");

//calculate average linkage
//matrices to store avg max and min distances
float avgdist[K][K],csum=0;
float mincdist[K][K],maxcdist[K][K];
float maxc,minc,distc;
maxc=0;
minc=99999999999;
int q,total=0;
printf("\n");
printf("\nAvg linkage distance matrix\n");
printf("\n");
//calculate distances btw each point of one cluster to the other
for(i=0;i<K;i++){
	for(j=0;j<K;j++){
		for(k=0;k<size;k++){
			if(cluster[k]==carray[i]){
			
				for(p=0;p<size;p++){
					if(cluster[p]==carray[j]){
						distc=getdist(k,p,dimentions);
						csum+=distc;
						//get min and max dist
						if(distc>maxc){
							maxc=distc;						
						}
						if(distc<minc){
							minc=distc;						
						}
						total++;
				
					}//end if
				}//end for p
			}//end if1
		}//end for k
	//printf("\ncsum bw %d and %d =%f, avg=%f",i,j,csum,csum/(float)total);
	avgdist[i][j]=csum/(float)total;
	maxcdist[i][j]=maxc;
	mincdist[i][j]=minc;
	//reset values	
	maxc=0;
	minc=99999999999;
	csum=0;
	total=0;
	}printf("\n"); //end for j
	
	

}//end for i
printf("\n********Final Report**********\n");
//intra cluster is stored at position (i,i) in the avglinkage matrix as it is for the same cluster
printf("\nIntra cluster Distance\n");
for(i=0;i<K;i++){
	for(k=0;k<K;k++){
		if(i==k){
			printf("\nBetween Cluster %d and %d ===> %f",i,k,avgdist[i][k]);
		}
	}
	printf("\n");

}

printf("\nInter cluster Distance\n");
printf("\nAvg linkage\n");
for(i=0;i<K;i++){
	for(k=0;k<K;k++){
		if(i!=k){
			printf("\nBetween Cluster %d and %d ===> %f",i,k,avgdist[i][k]);
		}
	}
	printf("\n");

}
printf("\nMax linkage\n");
for(i=0;i<K;i++){
	for(k=0;k<K;k++){
		if(i!=k){
			printf("\nBetween Cluster %d and %d ===> %f",i,k,maxcdist[i][k]);
		}
	}
	printf("\n");

}

printf("\nMin linkage\n");
for(i=0;i<K;i++){
	for(k=0;k<K;k++){
		if(i!=k){
			printf("\nBetween Cluster %d and %d ===> %f",i,k,mincdist[i][k]);
		}
	}
	printf("\n");

}


//free all the allocated space

free(carray);
free(cluster);
for (i = 0; i < numlines; i++){  
   free(data[i]);  
}  
free(data);

}// end main


float getdist(int index1,int index2,int dim){

int i,j;
float sum=0;
for(i=0;i<dim;i++){
//printf("\n%f -- %f",data[index1][i],data[index2][i]);
if(choice==1){
sum=sum+( (data[index1][i]-data[index2][i]) * (data[index1][i]-data[index2][i]) );
}
else{

sum=sum+(mod(data[index1][i]-data[index2][i]));
}

}

return sum;
}




float mod(float a){

if(a>0)
return a;
else
return -1*a;

}



//my attempt to calculate approx surface area of prots. reads .pdb file as input
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define PI 3.1423
#define mod(a)(a<0?(-1*a):(a))

int ind;
float *x, *y, *z;
int **adjc;
int *areatype;
float *SA;
char *type;
float *radius;
int totalatoms = 0;

int checkstr (char *);
void printx (char *);
void checkcontacts(void);

main (int argc, char **argv)
{

  FILE *fp, *fp1;
  char str[100];
  fp = fopen (argv[1], "r");
  int i, j;
  if (fp == NULL)
    {
      printf ("\nCannot open!!!!");
    }



//calculate total atoms to allocate space dynamically
  while (fgets (str, 100, fp) != NULL)
    {
      /* writing content to stdout */
      if (checkstr (str) == 1)
	{
	  // puts (str);
	  //fprintf (fp1, "%s", str);
	  // printx (str);

	  totalatoms++;
	}

    }


  printf ("\ntotal atoms are %d", totalatoms);


//allocate memory equall to totalatoms
  x = (float *) malloc (sizeof (float) * totalatoms);
  y = (float *) malloc (sizeof (float) * totalatoms);
  z = (float *) malloc (sizeof (float) * totalatoms);
  radius = (float *) malloc (sizeof (float) * totalatoms);
  type = (char *) malloc (sizeof (char) * totalatoms);
  areatype=(int *) malloc (sizeof (int) * totalatoms);	
  SA=(float *) malloc (sizeof (float) * totalatoms);
  

/*************************
   init the adjc matrix
************************/



/*******************************
extract coodinates and save in arrays
*******************************/

//store all x yz coordinates
//start with x coordinate 
  rewind (fp);
  ind = 0;
  while (fgets (str, 100, fp) != NULL)
    {

      if (checkstr (str) == 1)
	{
	  //  puts (str);
	  //fprintf(fp1,"%s",str);
	  // function to store coordinates in array
	  printx (str);

	}
    }


  fclose (fp);


//function to define radii for each atom
//printf("\nbefore func2total a=%d",totalatoms);
  for (i = 0; i < totalatoms; i++)
    {

      if (type[i] == 'C')
	{

	  radius[i] = 1.43;
	}
      else if (type[i] == 'O')
	{
	  radius[i] = 1.44;
	}

      else if (type[i] == 'N')
	{
	  radius[i] = 1.40;
	}

      else if (type[i] == 'S')
	{
	  radius[i] = 1.83;
	}
      else
	{
	  printf ("ERROR!!!! unkwnk= %c at %d", type[i], i);
	  exit (0);
	}

    }				//end for

/**********************************
  find and see contactpoints
***********************************/
//run function to see which have a contact circle
checkcontacts();

/*for(i=0;i<totalatoms;i++){
printf("\t%d",areatype[i]);
}*/





}//end main

int
checkstr (char *a)
{


  if ((strstr (a, "ATOM") != NULL))
    {
      if (a[77] == 'C' || a[77] == 'O' || a[77] == 'N' || a[77] == 'S')
	{
	  return 1;
	}
      return -1;
    }
  return -1;
}

void
printx (char *str)
{
  char tempx[20], tempy[20], tempz[20];

  int i;
  int j = 0;
  //printf ("\n");

//calculate x coordinate
  j = 0;
  for (i = 26; i <= 39; i++)
    {

      if (str[i] == ' ')
	{
	  continue;
	}
      tempx[j++] = str[i];
      //printf("%f",str[i]);


    }

  x[ind] = atof (tempx);
  // printf ("**%f", atof (temp));

//calculate y coordinate
  j = 0;
  for (i = 39; i <= 47; i++)
    {

      if (str[i] == ' ')
	{
	  continue;
	}
      tempy[j++] = str[i];
      //   printf("%c",str[i]);


    }

  y[ind] = atof (tempy);


//calculate z coordinate
  j = 0;
  for (i = 48; i <= 55; i++)
    {

      if (str[i] == ' ')
	{
	  continue;
	}
      tempz[j++] = str[i];
      //  printf("%c",str[i]);


    }

  z[ind] = atof (tempz);

//calculate type
  type[ind] = str[77];

  ind++;
}

void checkcontacts(void){

int i,j,ctr;
float R;
float X,Y,Z;
for(i=0;i<totalatoms;i++){
	areatype[i]=0;
	ctr=0;
	for(j=i+1;j<totalatoms;j++){
		R=radius[i]+radius[j];
		X=mod(x[i]-x[j]);
		Y=mod(x[i]-x[j]);
		Z=mod(x[i]-x[j]);
		
		if(X<R){
			if(Y<R){
				if(Z<R){
					areatype[i]=1;
					ctr++;
				}
			}
		}
	}//end for j
printf("\ntotal for atom %d=%d",i,ctr);
}//end for i

}//end func



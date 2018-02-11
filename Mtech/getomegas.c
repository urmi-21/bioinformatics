#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define PI 3.1423
#define max 14
//x y z to store coordinates
float *x, *y, *z;
int ind;
int checkstr (char *);
void returnnormal (float *, float, float, float, float, float, float, float,
		   float, float);

float getangle (float, float, float, float, float, float, float, float, float,
		float, float, float);

float returnangle (float *, float *);
float squareroot (float number);
float normal1[3], normal2[3];
void printx (char *);
int
main (int argc, char **argv)
{

  FILE *fp, *fp1;
  fp = fopen (argv[1], "r");
  fp1 = fopen ("fullextractedseq.txt", "w+");
  int totalatoms = 0, i, j;
  if (fp1 == NULL)
    {
      printf ("\nCannot open!!!!");
    }
//ctr and upperval to keep track how many atoms we need
  int ctr = 0, upperval = 15;
  if (fp == NULL)
    {
      printf ("\nFailed");
    }
  char str[100];

//calculate total atoms to allocate space dynamically
  while (fgets (str, 100, fp) != NULL)
    {
      /* writing content to stdout */
      if (checkstr (str) == 1)
	{
	  //  puts (str);
	  fprintf (fp1, "%s", str);
	  //printx (str);

	  totalatoms++;
	}

    }



//allocate memory equall to totalatoms
  x = (float *) malloc (sizeof (float) * totalatoms);
  y = (float *) malloc (sizeof (float) * totalatoms);
  z = (float *) malloc (sizeof (float) * totalatoms);

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
	  printx (str);

	}
    }




  fclose (fp);
  fclose (fp1);
//FIle to save results for plot
  FILE *fp2;
  fp2 = fopen ("omegas.txt", "w+");
  if (fp2 == NULL)
    {
      printf ("\nERROR opening");
      return 0;
    }
//calucalte agles
  float omegaangle[totalatoms / 4];
//calculate omega angle for all residues
//CA start at 1 so start i from 1

  j = 0;
  for (i = 1; i < max * 4; i = i + 4)
    {
      returnnormal (normal1, x[i], y[i], z[i], x[i + 1], y[i + 1], z[i + 1],
		    x[i + 3], y[i + 3], z[i + 3]);
      printf ("\nNormal to plane 1 is:");
      printf ("\n%fi+%fj+%fk\n", normal1[0], normal1[1], normal1[2]);
      fprintf (fp2, "\nNormal to plane 1 is:");
      fprintf (fp2, "\n%fi+%fj+%fk\n", normal1[0], normal1[1], normal1[2]);
      returnnormal (normal2, x[i + 1], y[i + 1], z[i + 1], x[i + 3], y[i + 3],
		    z[i + 3], x[i + 4], y[i + 4], z[i + 4]);
      printf ("\nNormal to plane 2 is:");
      printf ("\n%fi+%fj+%fk\n", normal2[0], normal2[1], normal2[2]);
      fprintf (fp2, "\nNormal to plane 2 is:");
      fprintf (fp2, "\n%fi+%fj+%fk\n", normal2[0], normal2[1], normal2[2]);
      omegaangle[j] = returnangle (normal1, normal2);

      printf ("Omega is = %f\n", omegaangle[j]);
      fprintf (fp2, "omega angle \t %f\n", omegaangle[j]);
      j++;

    }


  fclose (fp2);






  return 0;
}

int
checkstr (char *a)
{


  if ((strstr (a, "ATOM ") != NULL))
    {
      //check for N,CA,C or O

      if (a[13] == 'N' && a[14] == ' ')
	{

	  return 1;
	}
      if (a[13] == 'C' && a[14] == ' ')
	{

	  return 1;
	}

      if (a[13] == 'O' && a[14] == ' ')
	{

	  return 1;
	}

      if (a[13] == 'C' && a[14] == 'A' && a[15] == ' ')
	{

	  return 1;
	}

    }
  return -1;
}


void
printx (char *str)
{
  char tempx[20], tempy[20], tempz[20];

  int i;
  int j = 0;

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


  ind++;
}


void
returnnormal (float norm1[3], float p1x, float p1y, float p1z, float p2x,
	      float p2y, float p2z, float p3x, float p3y, float p3z)
{
//vectors p1p2 and p1p3
  float p1p2[3], p1p3[3];
//float normal[3];
  int i, j, k;
//calculate vector p1p2
  p1p2[0] = p2x - p1x;
  p1p2[1] = p2y - p1y;
  p1p2[2] = p2z - p1z;
//calculate vector p1p3
  p1p3[0] = p3x - p2x;
  p1p3[1] = p3y - p2y;
  p1p3[2] = p3z - p2z;
//calculate normal
  norm1[0] = 1 * ((p1p2[1] * p1p3[2]) - (p1p3[1] * p1p2[2]));
  norm1[1] = -1 * ((p1p2[0] * p1p3[2]) - (p1p3[0] * p1p2[2]));
  norm1[2] = 1 * ((p1p2[0] * p1p3[1]) - (p1p3[0] * p1p2[1]));



}

float
returnangle (float n1[3], float n2[3])
{

  float angle;
  float absn1, absn2;
  float n1cn2[3], n1dn2, mod;
  
//calculate dot product
  n1dn2 = (n1[0] * n2[0]) + (n1[1] * n2[1]) + (n1[2] * n2[2]);
//calculate n1Xn2
  n1cn2[0] = 1 * ((n1[1] * n2[2]) - (n2[1] * n1[2]));
  n1cn2[1] = -1 * ((n1[0] * n2[2]) - (n2[0] * n1[2]));
  n1cn2[2] = 1 * ((n1[0] * n2[1]) - (n2[0] * n1[1]));
//calculate mod n1cn2
  mod = (n1cn2[0] * n1cn2[0]) + (n1cn2[1] * n1cn2[1]) + (n1cn2[2] * n1cn2[2]);
  mod = squareroot (mod);

  angle = atan2 (mod, n1dn2) * (180.0 / PI);
  return angle;
}





float
squareroot (float num)
{
  if (num >= 0)
    {
      float x = num;
      int i;
      for (i = 0; i < 20; i++)
	{
	  x = (((x * x) + num) / (2 * x));
	}
      return x;
    }

}

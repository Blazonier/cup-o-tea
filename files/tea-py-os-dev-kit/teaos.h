int x = 0,y = 0;
char * vga  = (char *)0xB8000;

void printChar(char ch,int color){
  if(ch=='\n'||x==160){
      x=0;
      y++;
  }
  if(ch!='\n'){
      vga[(y*160)+x]=ch;
      vga[(y*160)+x+1]=color;
      x+=2;
  }
  if (y == 25)
  {
    y = 1;
  }

}

void cell(int ly, int lx, char ch, int color){
      vga[(ly*160)+lx]=ch;
      vga[(ly*160)+lx]=color;
      lx+=2;
}
void print(char * str,int color){
    for(int i =0;str[i]!=0;i++)
    {
      printChar(str[i],color);
    }
}
int candellch = 1;

void clear_screen_old(void)
{
    int index = 0;
    x = 0;
    y = 0;
    while (index < 80 * 25 * 2 ) {
            vga[index] = ' ', 0x000;
            index += 1;
    }
    x = 0;
    y = 0;
}

int bgcol = 0x000;

void clear_screen(int col)
{
    int index = 0;
    x = 0;
    y = 0;
    short * wide_vga_buffer = (short*)vga;
    while (index < 80 * 25) {
            wide_vga_buffer[index] = ' ' | (col << 8);
            index++;
    }
}
void dellch(){
  if (x == 2)
  {
    cell(y, x, 'A', 0x000);
    candellch = 0;
  }
  else
  {
    candellch = 1;
  }
  if (candellch == 1)
  {
    x -= 2;
  }
  if (x == 0 && candellch == 1)
  {
    x = 159;
    y -= 1;
    cell(y, x, 'A', 0x000);
  }
  if (candellch == 1)
  {
    cell(y, x, 'A', 0x000);
  }
}

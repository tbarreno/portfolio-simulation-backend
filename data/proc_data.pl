#!/usr/bin/perl
#
# Procesado inicial
#

$DATA_DIR="symbols-orig";
$OUTPUT_DIR="symbols";

# Bucle por cada fichero
opendir($dh, $DATA_DIR) || die("No se ha podido acceder al directorio $DATA_DIR\n");
while(readdir $dh) {
  if( /_data.csv$/ ) {
    procesa_fichero($_);
    exit(0);
  }
}
closedir $dh;

# Rutina de procesado
sub procesa_fichero($)
{
  my $filename = shift;
  my $input_file = "$DATA_DIR/$filename";
  my $output_file = "$OUTPUT_DIR/$filename";

  print(" * $DATA_DIR/$filename -> $OUTPUT_DIR/$filename\n");

  # Preparamos los datos
  my $header = "";
  my $current = "";

  # Abrimos el fichero
  open(my $fh, "< $input_file ") || die("No se ha podido abrir el fichero $input_file\n");
  while(<$fh>)
  {
    # La cabecera
    if( /^date/ )
    {
      $header = $_;
      next;
    }


  }
}

#Alberto Jahir Chavero Lara 1948878

$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "==Determinando tu gateway..."
Write-Host "Tu gateway: $subred"
#
#
$rango = $subred.Substring(0,$subred.IndexOf('.')+1+$subred.Substring($subred.IndexOf('.')+1).IndexOf('.')+3)
Write-Host "== Determinando tu rango de subred ..."
echo $rango
#
#
$punto = $rango.EndsWith('.')
if ($punto -like "False")
{
    $rango = $rango + '.'
}
#
#
$rango_ip=@(1..254)
Write-Output ""
Write-Host "--Subred actual:"
Write-Host "Escaneando: " -NoNewline ; Write-Host $rango -NoNewline; Write-Host "0/24" -ForegroundColor Red
#
#
foreach ($r in $rango_ip)
{
    $actual = $rango + $rango
    $responde = Test-connection $actual -Quiet -Count 1
    if ($responde -eq "True")
    {
        Write-Output ""
        Write-host "Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green
    }
}

$portstoscan= @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,636,1025,1443,3389,5985,8080,10000)
$waittime = 100
#
Write-Host "Direccion ip a escanear: " -NoNewline
$direccion = Read-Host
#
foreach ($p in $portstoscan)
{
    $TCPObject = new-object System.Net.Sockets.TcpClient
    try{ $resultado = $TCPObject.connectAsync($direccion,$p).Wait($waittime)}catch{}
    if ($resultado -eq "True")
    {
        Write-Host "Puerto abierto: " -NoNewline; Write-host $p -ForegroundColor Green
    }
}

#Fin del Script
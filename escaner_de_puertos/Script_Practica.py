#Alberto Jahir Chavero Lara 1948878
import nmap

def main():
    print('Selecciona opcion deseada :')
    print('1 Escaneo de  UDP')
    print('2 Escaneo Completo')
    print('3 Deteccion de sistema operativo actual')
    print('4 Escaneo de red actual  con ping')
    venus = int(input())
    triton = nmap.PortScanner()  
    if venus == 1:
        print(triton.scan('192.168.100.1', '1-1024', '-v -sU'))
    elif venus == 2:
        triton.scaner.scan('192.168.100.1', '1-1024', '-v -sU -o -p 22-80')
    elif venus == 3:
        triton.scan('192.168.100.1', '1-1024', '-v -sV -o')
    elif venus == 4:
        triton.scan('192.168.100.1', '1-1024', '-v -sP')



if __name__ == '__main__':
    main()
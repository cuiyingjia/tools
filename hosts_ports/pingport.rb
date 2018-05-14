require 'socket'    
include Socket::Constants            
def ping_port(address, port)           
  begin    
    socket = Socket.new(AF_INET, SOCK_STREAM, 0)          
    socket.connect(Socket.pack_sockaddr_in(port, address))     
    puts "Port:#{port} is Opened~"    
    socket.close     
  rescue 
    puts "Port:#{port} is not available!\n"   
  end            
end
ping_port("127.0.0.1",8080)#input here  
require 'socket'    
include Socket::Constants         
def scan(address, start_port, end_port)     
  threads = []     
  for port in start_port..end_port     
    threads << Thread.new(port) do |theport|     
      begin    
        socket = Socket.new(AF_INET, SOCK_STREAM, 0)     
        sockaddr = Socket.pack_sockaddr_in(theport, address)     
        socket.connect(sockaddr)     
        puts "Port:#{theport} is Opened\n"    
        socket.close     
      rescue    
      end    
    end    
  end    
  threads.each {|thr| thr.join}     
end
scan("127.0.0.1",8000,9080)#input here 
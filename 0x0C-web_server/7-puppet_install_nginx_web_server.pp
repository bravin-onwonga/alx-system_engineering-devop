exec { 'connect_to_server':
  command => 'ssh ubuntu@100.25.41.52',
}

package {'nginx':
  ensure => installed
}

$pub_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLj\
           J6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4\
           kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr\
           6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE7\
           0ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN'

$str = "Host *
    PasswordAuthentication no
    StrictHostKeyChecking no"

$server_str = "
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  root /var/www/html;

  index index.html index.htm index.nginx-debian.html;

  server_name _;

  location \ {
    try_files \$uri \$uri/ =404;
  }

  location /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }
}
"

exec { 'root_access':
  command => 'sudo su',
  path    => '/usr/bin/'
}

file { '/etc/ssh/sshd_config':
  ensure => present,
}

exec { 'update_ssh_config':
  command => "echo '${str}' | sudo tee /etc/ssh/sshd_config > /dev/null",
  path    => '/usr/bin/',
  require => File['/etc/ssh/sshd_config'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $server_str,
}

exec { 'add_key':
  command => "echo '${pub_key}' >> ~/.ssh/authorized_keys"
  path    => '/usr/bin/'
}

exec { 'restart_ssh_service':
  command => 'sudo service ssh restart',
  path    => '/usr/sbin:/sbin:/usr/bin:/bin',
  require => Exec['update_ssh_config'],
}

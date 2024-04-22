# Connect to your server using the private key
exec { 'connect_server" :
  command => 'echo ssh -i ~/.ssh/school ubuntu@server01',
  path    => '/usr/bin/echo'
}

# Changes to our configuration file
file { '/etc/ssh/sshd_config':
  ensure  => present,
  content => "Host *\n\tPasswordAuthentication no\n"
}

# Restart SSH service after making changes
service { 'ssh':
  ensure  => running,
  enable  => true,
  require => File['/etc/ssh/sshd_config'],
}

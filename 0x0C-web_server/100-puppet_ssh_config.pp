# Connect to your server using the private key
exec { 'connect_server" :
  command => 'ssh -i ~/.ssh/school ubuntu@35.153.226.28',
  path    => '/usr/bin'
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

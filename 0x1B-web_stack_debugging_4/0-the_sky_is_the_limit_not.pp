# Puppet file to debug failed request errors
file { '/etc/security/limits.conf':
  ensure => present,
}

exec { 'nofilelimits':
  command => 'echo "root soft nofile 100000 hard nofile 100000" | sudo tee -a /etc/security/limits.conf',
  path    => '/usr/bin/'
}

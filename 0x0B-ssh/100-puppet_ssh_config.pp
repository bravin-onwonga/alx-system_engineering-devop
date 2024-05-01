# Configure server using puppet
exec { 'connect_to_server':
  command => 'ssh ubuntu@100.25.41.52',
}

$str = "
Host *
  PasswordAuthentication no

Host client
  HostName 100.25.41.52
  IdentityFile ~/.ssh/school
  User client
"

file { '/etc/ssh/sshd_config':
  ensure => present,
  content => $str
}

exec { 'restart_ssh_service':
  command => 'sudo service ssh restart',
  path    => '/usr/sbin:/sbin:/usr/bin:/bin',
  require => Exec['update_ssh_config'],
}

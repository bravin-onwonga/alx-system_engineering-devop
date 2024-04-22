# Changes to our configuration file
file { '/etc/ssh/sshd_config':
  ensure => present
}

exec { 'add line to file':
  command => 'echo -e "Host *\n\tPasswordAuthentication no\n" > sshd_config'
}

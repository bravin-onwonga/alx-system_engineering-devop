# Changes to our configuration file
file { '/etc/ssh/sshd_config':
  ensure => file,
}
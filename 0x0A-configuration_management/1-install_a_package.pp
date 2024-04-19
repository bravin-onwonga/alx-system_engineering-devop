# Installs a package flask using pip3
package { ['python3-pip']:
  ensure => installed,
}

package { 'Flask':
  require  => Package['python3-pip'],
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Installs a package flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  install_options => '-q',
}

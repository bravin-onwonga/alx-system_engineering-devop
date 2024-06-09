# Puppet file to fix internal server error

exec { '500-error-fix':
  command => 'sed -i s|phpp|php|g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/'
}

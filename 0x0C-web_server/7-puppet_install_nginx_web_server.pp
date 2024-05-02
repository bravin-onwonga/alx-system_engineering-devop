# Sets up a server to allow login and serve some pages and redirects
$str="
    Host *
        PasswordAuthentication no
        StrictHostKeyChecking no
"

$server_str="
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
            try_files \$uri \$uri/ =404;
        }

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
    }
"

package {'nginx':
  ensure => installed
}

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
  require => File['/etc/ssh/sshd_config']
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => $server_str,
  require => Package['nginx']
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n"
}

exec { 'reload_nginx':
  command => 'echo nginx -s reload',
  path    => '/usr/bin/',
  require => Package['nginx']
}

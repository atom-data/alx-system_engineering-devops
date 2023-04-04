# create a custom http header
$file_path = '/etc/nginx/sites-available/default'
exec { 'add_header_x-served-by':
  command     => "sudo sed -i \\
                  '/^[^#]*server {/,/^}$/ \\
                  s/^\\( *\\)\\(server {\\)$/\\1\\2\\n\\1\\tadd_header X-Served-By ${::hostname};/' \\
                  ${file_path}",
  path        => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  refreshonly => true,
}

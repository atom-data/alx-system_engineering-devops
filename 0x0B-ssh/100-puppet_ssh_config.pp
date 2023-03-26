#change ssh client configurations
$contents = "Host *\n\tPasswordAuthentication yes\n\nHost 54449-web-01\n\tHostname 100.26.244.193\n\tUser ubuntu\n\tPubKeyAuthentication yes\n\tPreferredAuthentications publickey\n\tIdentityFile ~/.ssh/school\n\tIdentitiesOnly yes\n\tPasswordAuthentication no"
file { '/root/.ssh/config':
 ensure  => 'file',
 path    => '/root/.ssh/config',
 mode    => '0644',
 content => $contents
}

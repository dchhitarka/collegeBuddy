var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
	  '',
    '/settings',
    '/settings/general',
    '/settings/manage',
	  '{% static "js/main.js"%}',
	  '{% static "js/config.js"%}',
	  '{% static "js/genral.js"%}',
	  '{% static "js/manage.js"%}',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        return cache.addAll(urlsToCache).then(() => self.skipWaiting())
      })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(CACHE_NAME)
      .then(cache => cache.match(event.request, {ignoreSearch: true}))
      .then(response => {
      return response || fetch(event.request);
    })
  );
});

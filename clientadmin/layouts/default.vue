<template>
  <div class="">
    <div class="level px-4 py-2 is-mobile is-hidden-desktop" style="border-bottom: 1px solid #dbdbdb">
      <div class="level-left">
        <figure class="image mt-1">
          <img src="~assets/arraycase-b.svg" style="width:120px;" alt="" />
        </figure>
      </div>
      <div class="level-right">
        <button class="button " @click="openSidebar = !openSidebar">
          <b-icon icon="menu" class="mr-2"></b-icon>
          <span>

            Menu
          </span>
        </button>
      </div>
    </div>


    <b-sidebar type="is-white" fullheight fullwidth overlay right v-model="openSidebar">
      <div class="level is-hidden-touch px-4 py-4 is-mobile is-hidden-desktop" style="border-bottom: 1px solid #dbdbdb">
        <div class="level-left">
          <figure class="image mt-1">
            <img src="~assets/arraycase-b.svg" style="width:120px;" alt="" />
          </figure>
        </div>
        <div class="level-right">
          <button class="button" @click="openSidebar = !openSidebar">
            <b-icon icon="window-close" class="mr-2"></b-icon>
            <span>

              Close
            </span>
          </button>
        </div>
      </div>
      <div class="sidebar-content-body pl-2 mx-0 pb-4">
        <!-- <header class="has-text-centered"></header> -->
        <section class="sidebar-content-main">
          <div class="menu sticky is-fullheight px-0">


            <nuxt-link v-for="(nav, index) in navigation" :key="index + '_side_nav'" class="button-x is-fullwidth pl-3"
              to="/">
              <b-icon class="mr-3" :icon="nav.icon"></b-icon>
              <span class="">{{ nav.name }}</span>
            </nuxt-link>


          </div>
        </section>
        <footer class="mx-3">
          <div class="media my-2 ">
            <div class="media-left">
              <b-icon icon="account-circle"></b-icon>

            </div>
            <div class="media-content">
              <p class="">Padam Sethia</p>
              <p class="heading">ADMIN</p>
            </div>
            <div class="media-right">
              <button class="button is-light">

                <b-icon icon="dots-vertical"></b-icon>
              </button>
            </div>
          </div>
          <div class="media my-2">
            <div class="media-left">
              <b-icon icon="bell"></b-icon>

            </div>
            <div class="media-content">
              <p class="">Notifications</p>
              <p class="heading">0 Updates</p>
            </div>
            <div class="media-right">
              <button class="button is-light">

                <b-icon icon="arrow-top-right"></b-icon>
              </button>
            </div>
          </div>
        </footer>
      </div>
    </b-sidebar>

    <!-- Desktop Nav Layout -->

    <div class="columns">
      <div class="column is-hidden-touch pr-0 is-2 mt-0 pt-0 mb-0 pb-0" style="border-right: 1px solid #dbdbdb">
        <div class="sidebar-content-body px-3  mx-0 my-2 pb-4">
          <header class="has-text-centered pt-4">

          </header>
          <section class="sidebar-content-main">

            <div class="menu sticky is-fullheight px-0">

              <div v-for="(nav, index) in navigation" :key="index + '_side_nav'">
                <nuxt-link v-if="!nav.nested" class="button-x is-fullwidth pl-3" to="/">
                  <div class="media">
                    <div class="media-left">
                      <b-icon class="" :icon="nav.icon"></b-icon>

                    </div>
                    <div class="media-content is-fullwidth">

                      <span class="">{{ nav.name }}</span>
                    </div>

                  </div>
                </nuxt-link>
                <div v-else>
                  <b-collapse :open="false" animation="slide" aria-id="contentIdForA11y1">
                    <template #trigger="props">
                      <div class="button-x is-fullwidth pl-3">
                        <div class="media">
                          <div class="media-left">
                            <b-icon class="" :icon="nav.icon"></b-icon>

                          </div>
                          <div class="media-content is-fullwidth">

                            <span class="">{{ nav.name }}</span>
                          </div>
                          <div class="media-right">

                            <b-icon class="is-pulled-right" :icon="!props.open ? 'chevron-down' : 'chevron-up'"></b-icon>
                          </div>
                        </div>

                      </div>
                    </template>
                    <div class="">
                      <nuxt-link v-for="(sub_nav, index) in navigation.nested" :key="index + '_sub_nav'"
                        class="button-x is-fullwidth pl-6" :to="sub_nav.to">
                        <!-- <b-icon class="mr-3" :icon="nav.icon"></b-icon> -->
                        <span class="">{{ sub_nav.name }}</span>
                      </nuxt-link>
                    </div>
                  </b-collapse>

                </div>
              </div>


            </div>
          </section>
          <footer class="is-relative" style="width:100%;bottom: 0px !important; position: fixed">
            <b-dropdown expanded position="is-top-left" append-to-body aria-role="menu">
              <template #trigger="{ active }">
                <div class="level is-clickable user-box notification is-link is-light py-3 px-3">
                  <div class="level-left pr-0 mr-0">
                    <div class="level-item">

                      <b-icon icon="account-circle"></b-icon>
                    </div>

                    <div class="level-item ml-3">
                      <div>

                        <p class="">Padam Sethia</p>
                        <p class="heading">ADMIN</p>
                      </div>
                    </div>
                  </div>
                  <div class="level-right">
                    <button class="button level-item is-text ">

                      <b-icon icon="dots-vertical" class="has-text-link"></b-icon>
                    </button>
                  </div>
                </div>
              </template>


              <b-dropdown-item has-link aria-role="menu-item">
                <nuxt-link to="/" class="media button-x has-text-dark ">
                  <div class="media-left">
                    <b-icon icon="archive"></b-icon>
                  </div>
                  <div class="media-content">
                    <p class="">View Logs</p>

                  </div>
                </nuxt-link>

              </b-dropdown-item>
              <hr class="my-2 dropdown-divider">
              <b-dropdown-item has-link aria-role="menu-item ">
                <div class="media button-x px-3  has-text-danger ">
                  <div class="media-left">
                    <b-icon icon="exit-to-app"></b-icon>
                  </div>
                  <div class="media-content">
                    <p class="">Logout</p>

                  </div>
                </div>

              </b-dropdown-item>
            </b-dropdown>

          </footer>
        </div>
      </div>
      <div class="column">
        <div class="section  py-2" style="border-bottom:1px solid #dbdbdb">
          <div class="level">
            <div class="level-left">
              <b-breadcrumb class="level-item" size="is-normal" align="is-left">
                <b-breadcrumb-item tag='router-link' to="/">Home</b-breadcrumb-item>
                <b-breadcrumb-item tag='router-link' class="is-capitalized" :key="index + '_crumb'"
                  v-for="(crumb, index) in crumbs" :to="crumb.to">{{ crumb.title.replace('_', ' ')
                  }}</b-breadcrumb-item>
              </b-breadcrumb>

            </div>
            <div class="level-right">
              <div class="level-item button is-rounded disabled">
                <span class="">
                  <b-icon icon="magnify" class="has-text-grey mr-5"></b-icon>
                </span>
                <span class="tag">
                  Alt
                </span>
                +
                <span class="tag">
                  Q
                </span>
                for Global search
              </div>
              <button class="button level-item is-text">
                <b-icon icon="bell"></b-icon>
              </button>
            </div>
          </div>
        </div>
        <section class="section pt-5">
          <transition name="fade">
            <div>
              <nuxt />
            </div>
          </transition>
        </section>
      </div>
    </div>


  </div>
</template>
 
<script>
export default {
  // middleware: ["auth-user"],
  watch: {
    $route(to, from) {
      this.openSidebar = false;
    },
  },
  computed: {
    crumbs() {
      const route = this.$route

      const pathArray = route.path.split('/')
      pathArray.shift()
      const crumbs = pathArray.reduce((breadcrumbArray, path, idx) => {
        breadcrumbArray.push({
          to: !!breadcrumbArray[idx - 1]
            ? breadcrumbArray[idx - 1].to + '/' + path
            : '/' + path,
          title: path.toString().replace('-', ' '),
        })
        return breadcrumbArray
      }, [])
      return crumbs
    },
  },
  data() {
    return {
      expandOnHover: false,
      mobile: "reduce",
      openSidebar: false,
      reduce: false,
      navigation: [
        {
          'name': 'Home',
          'to': '/',
          'icon': 'home-variant',
        },
        {
          'name': 'All Employees',
          'to': '/',
          'icon': 'account-supervisor-circle',
        },
        {
          'name': 'Attendence',
          'to': '/',
          'icon': 'hail',
        },
        {
          'name': 'Business',
          'to': '/',
          'icon': 'office-building',
        },
        {
          'name': 'Reports',
          'to': '/',
          'icon': 'chart-pie',
        },

        {
          'name': 'Basic Masters',
          'to': '/',
          'icon': 'layers',
          'nested': [
            {
              'name': 'Location',
              'to': '/basic_master/product_category',
            }
          ]
        },

        {
          'name': 'Settings',
          'to': '/',
          'icon': 'cog',
        },
      ],
      app_switcher: [
        {
          'name': 'E-Catalogue',
          'to': 'https://jaitexart.in',
          // 'icon': 'home-variant',
        },
      ]
    };
  },
  methods: {
    async logout() {
      await this.$auth.logout().then((response) => {
        this.$router.push("/auth");
      });
    },
  },
};
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');

* {
  font-family: 'Inter', sans-serif;

}

li a.nuxt-link-exact-active.nuxt-link-active {
  color: grey;
}

hr {
  background-color: #dbdbdb;
  height: 1px;
}

html {
  scroll-behavior: smooth;
}

.user-box {
  border: 1px solid transparent;
  transition: 0.2s all ease-in;
  border-radius: 7px
}

.user-box:hover {
  border: 1px solid #552fbc88
}

.sidebar-content-body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

.sidebar-content-main {
  flex: 1;
}

.button-x {
  color: #0a0a0a;
  font-weight: 500;
  width: 100%;

  cursor: pointer;
  justify-content: left;
  padding: 0.5rem 0 0.5rem 0;
  /* padding-bottom: calc(0.7em - 1px);

  padding-top: calc(0.7em - 1px); */
  text-align: left;
  vertical-align: center;
  display: flex;
  white-space: nowrap;
  transition: 0.2s all ease-in;
}

.button-x-center {
  justify-content: center;
  text-align: center;
}

.button-x:hover {
  background-color: rgb(228, 228, 228);
  border-radius: 3px;
  color: #0a0a0a !important;
}

.sub-nav .button-x {
  padding: 10px 10px;
  font-weight: 300 !important;
}

.sub-nav .button-x:hover {
  font-weight: 300;
}

.menu-burger {
  cursor: pointer;
  display: block;
  height: 3.25rem;
  position: relative;
  width: 3.25rem;
  margin-left: auto;
  padding: 10px 10px 5px 0;
}

.is-family-monospace {
  font-family: "Roboto Mono";
  text-transform: uppercase;
}

.th-wrap {
  color: black;
  font-weight: 600;
}

.modal-content {
  overflow-y: auto !important;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}

li {
  list-style: none;
}
</style>